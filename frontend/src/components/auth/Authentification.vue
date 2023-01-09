<script lang="ts" setup>
import { ref, onMounted } from "vue";
import { CartItem, ShoppingSession, User } from "@/models";
import {
  create_user,
  read_users,
  toast_function,
  read_last_one_shopping_session_byuser,
  read_cart_items_by_sessionid,
  create_shopping_session,
} from "@/services/crud";
import { useAppStore } from "@/stores";
import { storeToRefs } from "pinia";
import { Form } from "vee-validate";
import * as Yup from "yup";
import InputField from "./InputField.vue";
import { useToast } from "vue-toast-notification";
import { useRouter } from "vue-router";

/** call localStorage */
const localStorage = window.localStorage;

/** get values from the stores */
const {
  list_user,
  current_user,
  list_cart_item,
  current_shopping_session,
  isAdminStore,
} = storeToRefs(useAppStore());

/** routing */

const router = useRouter();
const show = ref(true);

const toggle = () => {
  show.value = !show.value;
};

/** initialize userLoggin in store to false */

// isLoggedIn.value = false

onMounted(async () => {
  list_user.value = (await read_users()).map((res: any) => {
    return res;
  });
});

/** check existence of email in the db*/
const check_email = (my_email: string, my_pass: string) => {
  let res: Boolean = false;
  list_user.value.forEach((element) => {
    if (element.email == my_email && element.password == my_pass) {
      current_user.value = element;
      // add user id to localstorage
      localStorage.setItem("userId", "" + JSON.stringify(element));
      localStorage.setItem("isLoggedIn", "true");
      const value = localStorage.getItem("userId");
      const user_obj = JSON.parse(value!);
      if (user_obj?.is_admin) {
        localStorage.setItem("isAdmin", "true");
        isAdminStore.value = true;
        console.log("this is an admin");
      } else {
        localStorage.setItem("isAdmin", "false");
        isAdminStore.value = false;
        console.log("this is not an admin");

      }

      current_user.value = user_obj;
      res = true;
    }
  });
  return res;
};

/** onsubmit signup */
const onSignUp = async (values: any) => {
  if (!check_email(values.email, values.password)) {
    const response = await create_user({
      telephone: values.phone,
      email: values.email,
      username: values.username,
      firstname: values.firstname,
      password: values.password,
      created_date: new Date(),
      is_admin: false,
    });

    toast_function("You are successfully signed up!", "success");
  } else {
    toast_function("Sorry email is already taken", "error");
  }
};
/** get last shopping session in db */

/** onsubmit login */
const onLogin = async (values: any) => {
  const $toast = useToast();
  // if log in success
  console.log(values.email);
  console.log(values.password);
  console.log(check_email(values.email, values.password));
  if (check_email(values.email, values.password)) {
    // initialize isLoggedIn store value
    // isLoggedIn.value = true

    // get last shopping session for user logged in
    let response_read_last_shopping =
      await read_last_one_shopping_session_byuser(current_user.value?.id!);
    // if shopping session for user logged in exist
    if (response_read_last_shopping != null) {
      console.log(response_read_last_shopping);
      console.log("last shopping sesssion id: ");
      console.log(response_read_last_shopping.id);
      // check if there is an cartitem inside the shopping session
      // get last cart item for a shopping session
      let response_list_cart_item = await read_cart_items_by_sessionid(
        response_read_last_shopping.id!
      );

      // assign to list_cart_item cart items from db
      // response_list_cart_item.forEach((element:CartItem) => {
      //   list_cart_item.value.push(element)
      // })
      // if cart items are not empty
      console.log("list cart items last session: ");
      console.log(response_list_cart_item);
      if (response_list_cart_item != null) {
        console.log("list cart item not null");
        list_cart_item.value = response_list_cart_item;
      } else {
        console.log("list cart item null");
      }
    } else {
      console.log("not an existence session yet! ");
    }

    // create a new variable of shopping session
    let shopping_session = new ShoppingSession({
      user_id: current_user.value?.id,
      total: 0,
      created_date: new Date(),
    });

    // add shopping session to database
    const response_create_shop_sess = await create_shopping_session(
      shopping_session
    )
      .then((res) => console.log("shopping session created successfully"))
      .catch((error) => console.log(error));
    // get last shopping session
    let response_read_last_shopping_after_create =
      await read_last_one_shopping_session_byuser(current_user.value?.id!);
    // add to current_shopping_session new created shopping session
    current_shopping_session.value = response_read_last_shopping_after_create;
    console.log("current_shopping_session.value");
    console.log(current_shopping_session.value);

    toast_function("You are successfully logged in!", "success");
    setTimeout(() => {
      router.push({
        name: "home",
        replace: true,
      });
    }, 1000);
  } else {
    toast_function(
      "Sorry, wrong email or password! Do you have an account ?",
      "error"
    );
  }
};

/** on invalid submit */
const onInvalidSubmit = () => {
  console.log("invalid button me");
  const submitBtn = document.querySelector(".auth-btn");
  submitBtn!.classList.add("invalid");
  setTimeout(() => {
    submitBtn!.classList.remove("invalid");
  }, 1000);
};

/** use Yup to generate a login validation schema */
const schema_login = Yup.object().shape({
  email: Yup.string().email().required(),
  password: Yup.string().min(1).required(),
});

/** use Yup to generate a signup validation schema */
const schema_signup = Yup.object().shape({
  username: Yup.string().required(),
  firstname: Yup.string().required(),
  email: Yup.string().email().required(),
  phone: Yup.string()
    .required()
    .min(1)
    .oneOf([Yup.ref("phone")], "Phone number must be at least 9 digits"),
  password: Yup.string().min(1).required(),
  confirm_password: Yup.string()
    .required()
    .oneOf([Yup.ref("password")], "Passwords do not match"),
});
</script>
<template>
  <section class="mb-5" style="background-color: transparent">
    <!-- gradient-form -->
    <div class="container py-5 h-80">
      <div class="row d-flex justify-content-center align-items-center h-80">
        <div class="col-xl-10">
          <div class="card rounded-3 text-black">
            <div class="row">
              <div class="col-lg-6">
                <div class="card-body p-md-5 mx-md-4">
                  <div class="text-center">
                    <h4 v-if="show" class="mt-1 mb-5 pb-1">Log In</h4>
                    <h4 v-else class="mt-1 mb-5 pb-1">Sign Up</h4>
                    <!-- <p>Please login to your account</p> -->
                    <div v-if="show">
                      <Form
                        @submit="onLogin"
                        :validation-schema="schema_login"
                        @invalid-submit="onInvalidSubmit"
                      >
                        <InputField
                          name="email"
                          type="text"
                          label="Email"
                          placeholder="Your email"
                          success-message="Email address correct !"
                        />
                        <InputField
                          name="password"
                          type="password"
                          label="Password"
                          placeholder="Your Name"
                          success-message="Password is correct!"
                        />
                        <div class="text-center pt-1 mb-5 pb-1">
                          <button
                            class="auth-btn btn btn-outline-warning btn-block"
                            type="submit"
                          >
                            <!--@click="addUser()"-->
                            Log In
                          </button>
                          <br /><br /><br />
                          <a class="text-muted" href="#!">Forgot password?</a>
                        </div>
                      </Form>
                    </div>
                    <!-- Please sign up -->
                    <div v-else>
                      <Form
                        @submit="onSignUp"
                        :validation-schema="schema_signup"
                        @invalid-submit="onInvalidSubmit"
                      >
                        <InputField
                          name="username"
                          type="text"
                          label="Username"
                          placeholder="Your username"
                          success-message="Nice to meet you Mr you!"
                        />
                        <InputField
                          name="firstname"
                          type="text"
                          label="Firstname"
                          placeholder="Your firstname"
                          success-message="Glad to know you !"
                        />
                        <InputField
                          name="email"
                          type="email"
                          label="Email"
                          placeholder="example@google@com"
                          success-message="We won't spam you!"
                        />
                        <InputField
                          name="phone"
                          type="number"
                          label="Phone number"
                          success-message="Just to keep in touch!"
                        />
                        <InputField
                          name="password"
                          type="password"
                          label="Password"
                          placeholder="Your password"
                          success-message="Nice and secure!"
                        />
                        <InputField
                          name="confirm_password"
                          type="password"
                          label="Confirm Password"
                          placeholder="Type it again"
                          success-message="Glad you remembered it!"
                        />

                        <div class="text-center pt-1 mb-5 pb-1">
                          <button
                            class="auth-btn btn btn-outline-warning btn-block"
                            type="submit"
                          >
                            <!--@click="addUser()"-->
                            Sign Up
                          </button>
                          <!-- <a class="text-muted" href="#!">Forgot password?</a> -->
                        </div>
                      </Form>
                    </div>
                    <div
                      class="d-flex align-items-center justify-content-center pb-4"
                    >
                      <!-- <p class="mb-0 me-2">Don't have an account?</p> <a href="#"> Please Sign Up! </a>
                      <p class="mb-0 me-2">Don't have an account?</p> <a href="#"> Please Sign Up! </a> -->
                      <!-- <button type="button" class="btn btn-outline-danger">Create new</button> -->
                    </div>
                  </div>
                </div>
              </div>
              <div
                class="col-lg-6 d-flex align-items-center"
                style="background: #d35400"
              >
                <!-- gradient-custom-2 -->
                <div class="text-white px-3 py-4 p-md-5 mx-md-4">
                  <h4 class="mb-4">We are here to change your life...</h4>
                  <p class="small mb-0">
                    Lorem ipsum dolor sit amet, consectetur adipisicing elit,
                    sed do eiusmod tempor incididunt ut labore et dolore magna
                    aliqua. Ut enim ad minim veniam, quis nostrud exercitation
                    ullamco laboris nisi ut aliquip ex ea commodo consequat.
                  </p>
                  <button class="btn_signup" @click="toggle">
                    <span v-if="show">Sign Up</span>
                    <span v-else>Log In</span>
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
<style scoped>
.list-unstyled li a {
  width: 45px;
  height: 45px;
  line-height: 45px;
  border-radius: 50%;
  font-size: 16px;
  border-radius: 40%;
  border: 1px solid rgba(255, 255, 255, 0.3);
}
.btn_signup {
  box-sizing: border-box;
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  width: 200px;
  font-size: 16px;
  font-weight: 600;
  color: #fff;
  cursor: pointer;
  margin: 20px;
  height: 55px;
  text-align: center;
  border: none;
  background-size: 300% 100%;

  border-radius: 50px;
  -moz-transition: all 0.4s ease-in-out;
  -o-transition: all 0.4s ease-in-out;
  -webkit-transition: all 0.4s ease-in-out;
  transition: all 0.4s ease-in-out;
  background-image: linear-gradient(
    to right,
    #fc6076,
    #ff9a44,
    #ef9d43,
    #e75516
  );
  box-shadow: 0 4px 15px 0 rgba(252, 104, 110, 0.75);
}
.auth-btn.invalid {
  animation: shake 0.5s;
  animation-iteration-count: infinite;
}
.btn_signup:hover {
  background-position: 100% 0;
  -moz-transition: all 0.4s ease-in-out;
  -o-transition: all 0.4s ease-in-out;
  -webkit-transition: all 0.4s ease-in-out;
  transition: all 0.4s ease-in-out;
}

.btn_signup:focus {
  outline: none;
}
</style>
