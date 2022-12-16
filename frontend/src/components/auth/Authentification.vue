<script lang="ts" setup>
    import { ref,onMounted } from "vue"
    import { ShoppingSession, User } from "@/models";
    import { create_user,read_users, toast_function , 
      create_shopping_session, read_shopping_sessions, read_cart_items, read_last_one_shopping_session_byuser} from "@/services/crud";
    import { useAppStore } from "@/stores";
    import { storeToRefs } from "pinia";
    import { Form } from 'vee-validate';
    import * as Yup from 'yup';
    import InputField from "./InputField.vue";
    import {useToast} from 'vue-toast-notification';
    import { decodeCredential, googleLogout } from "vue3-google-login";
    import { useRouter } from 'vue-router';
    
    /** get values from the stores */
    const { list_category, list_user, current_user, isLoggedIn, list_cart_item,
       list_shopping_Session , last_shopping_session, current_shopping_session} = storeToRefs(useAppStore())

    const get_last_shoppsession_db = (list_shop_sess_db:Array<ShoppingSession>):boolean => {

      let found = false
      let count = 0
      list_shop_sess_db.forEach((element:ShoppingSession) => {
        
        // iterate through user list
        list_user.value.forEach((user_item:User) => {
            // if user id is found in list shopping sesssion, get the last element
            if (user_item.id == element.user_id) {
              last_shopping_session.value = element
              found = true
              count+=1
            }
          })
        })
      console.log("count value: ",count)
      return found
    }

    const get_current_shoppsession_db = (list_shop_sess_db:Array<ShoppingSession>):boolean => {

      let found = false
      let count = 0
      list_shop_sess_db.forEach((element:ShoppingSession) => {

        // iterate through user list
        list_user.value.forEach((user_item:User) => {
            // if user id is found in list shopping sesssion, get the last element
            if (user_item.id == element.user_id) {
              current_shopping_session.value= element
              found = true
              count+=1
            }
          })
        })
      console.log("count value: ",count)
      return found
    }

    /** routing */

    const router = useRouter()
    const show = ref(true)

    const toggle = () => {
        show.value = !show.value
    }

    
    /** initialize userLoggin in store to false */
    isLoggedIn.value = false
    async function digestMessage(message:string) {
        const encoder = new TextEncoder();
        const data = encoder.encode(message);
        const hash = await crypto.subtle.digest('SHA-256', data);
        // console.log("hash me")
        // console.log(hash)
        return hash;
      }
      digestMessage("dkjfsljhefjhkj")
          // .then((digestBuffer) => console.log(digestBuffer.byteLength));
    /** security of password a voir avec crypto JS */ 
   
    onMounted(async () => {
      // console.log("display users: ")
      list_user.value = (await read_users()).map((res:any) => {
            return res;
        })
    })

    /** check existence of email in the db*/
    const check_email = ((my_email:string, my_pass:string)  => {
      let res:Boolean = false;
      list_user.value.forEach(element => {
        // console.log(element.email)
        if (element.email === my_email && element.password === my_pass) {
          current_user.value = element
          res = true
        }
      })
      return res
    })
    
    /** onsubmit signup */
    const onSignUp = (async (values:any) => {
      
      if (!check_email(values.email,values.password)) {
        // const response = await create_user({
        //   "telephone":values.phone,
        //   "email":values.email,
        //   "username":values.username,
        //   "firstname":values.firstname,
        //   "password":values.password,
        //   "created_date": new Date(),
        //   "is_admin": false})
        
        toast_function("You are successfully signed up!","success")
      }
      else {
        toast_function("Sorry email is already taken","error")
      }
  
    })
    /** get last shopping session in db */
    
    /** onsubmit login */
    const onLogin =  (async (values:any) => {
      const $toast = useToast();
      // if log in success
      if (check_email(values.email,values.password)) {

        // initialize isLoggedIn store value
        isLoggedIn.value = true

        // get last shopping session for a user loggedin
        let found = false
        let response_read_last_shopping = await read_last_one_shopping_session_byuser(current_user.value?.id!)
        last_shopping_session.value = response_read_last_shopping
        // create a new variable of shopping session
        let shopping_session = new ShoppingSession({
          "user_id": current_user.value?.id,
          "total": 0,
          "created_date": new Date(),
        })

        // if shopping session exists
        if(found = true) { 
            // get cartItem corresponding to shopping session
            let cart_items_db = await read_cart_items()
            console.log("read cart items in db: ")
            console.log(cart_items_db) 
            // list_cart_item.value = cart_items_db                
            console.log("shopping session for user exist last shopping session")
            console.log(last_shopping_session.value)
            if (list_cart_item.value.length != 0) {
              console.log(list_cart_item.value.length)
            }
            // let found = get_last_shoppsession_db(list_shop_sess_db)

        } else {
          console.log("shopping session for user does not exist")
          
        }

        // add shopping session to database
        const response_create_shop_sess = await create_shopping_session(shopping_session)
                      .then((res) => console.log("shopping session created successfully"))
                      .catch((error) => console.log(error))

        // initialize current shopping session values 
        // get_current_shoppsession_db(list_shop_sess_db)
        console.log("current shopping session: ")
        let response_read_one_shopping_session = await read_last_one_shopping_session_byuser(current_user.value?.id!)
        current_shopping_session.value = response_read_one_shopping_session
        console.log(current_shopping_session.value)
        toast_function("You are successfully logged in!","success")
        setTimeout(() => {
            router.push({
            name: 'home',
            replace:true
          })
        },1000)

      }
      else {
        toast_function("Sorry, wrong email or password! Do you have an account ?","error")
      }
    })

     /** login sso */
     const onSSOLogin = (response:any) => {
      const userData = decodeCredential(response.credential)
      console.log("Handle the userData: "+userData)
      // if email does not exist 
      // if (!check_email(userData.email)) {
      //   save user data
      //   const response = await create_user({
      //     "telephone":userData.phone,
      //     "email":userData.email,
      //     "username":userData.username,
      //     "firstname":userData.firstname,
      //     "password":userData.password,
      //     "created_date": new Date(),
      //     "is_admin": false})
      //   console.log("email does not exist")
      //   console.log("Handle the userData", userData)
      // }
      // if not 

      
    }

    /** on invalid submit */
    const onInvalidSubmit = (()=> {
      console.log('invalid button me')
      const submitBtn = document.querySelector('.auth-btn');
      submitBtn!.classList.add('invalid');
      setTimeout(() => {
        submitBtn!.classList.remove('invalid');
      }, 1000);
    })

    /** use Yup to generate a login validation schema */
    const schema_login = Yup.object().shape({
      email: Yup.string().email().required(),
      password: Yup.string().min(6).required()
    })

    /** use Yup to generate a signup validation schema */
    const schema_signup = Yup.object().shape({
      username: Yup.string().required(),
      firstname: Yup.string().required(),
      email: Yup.string().email().required(),
      phone: Yup.string().required().min(9)
          .oneOf([Yup.ref('phone')], 'Phone number must be at least 9 digits'),
      password: Yup.string().min(1).required(),
      confirm_password: Yup.string()
        .required()
        .oneOf([Yup.ref('password')], 'Passwords do not match'),
    })

</script>
<template>
<section class="mb-5" style="background-color:transparent;">
  <!-- gradient-form -->
  <div class="container py-5 h-80">
    <div class="row d-flex justify-content-center align-items-center h-80">
      <div class="col-xl-10">
        <div class="card rounded-3 text-black">
          <div class="row">
            <div class="col-lg-6">
              <div class="card-body p-md-5 mx-md-4">
                <div class="text-center">
               
                  <h4 v-if="show" class="mt-1 mb-5 pb-1">Log In </h4>
                  <h4 v-else class="mt-1 mb-5 pb-1 ">Sign Up </h4>
                    <!-- <p>Please login to your account</p> -->
                  <div v-if="show">
                      <Form @submit="onLogin"
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
                              <button class="auth-btn btn btn-outline-warning btn-block" type="submit"> <!--@click="addUser()"-->
                                  Log In
                              </button> <br><br><br>
                              <a class="text-muted" href="#!">Forgot password?</a>
                            </div>
                      </Form>
                      <p>Or Login With </p>
                      <GoogleLogin :callback="onSSOLogin"/> <!--prompt-->
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
                        <button class="auth-btn btn btn-outline-warning btn-block" type="submit"> <!--@click="addUser()"-->
                            Sign Up
                        </button>
                        <!-- <a class="text-muted" href="#!">Forgot password?</a> -->
                      </div>
                    </Form>
                </div>
                  <!--<p class="text-center" v-if="show">Or Log in with:</p>
                  <p class="text-center" v-else>Or Sign Up with:</p>
                   list of icons to log in social media -->
                  <!-- <div class="d-flex align-items-center justify-content-center pb-4">
                      <ul class="list-unstyled d-flex">
                          <li>
                              <a href="#" class="me-4">
                                  <font-awesome-icon icon="fa-brands fa-linkedin" size="lg" :style="{ color: 'black' }"/>
                              </a>
                          </li>
                          <li>
                              <a href="#" class="me-4">
                                  <font-awesome-icon icon="fa-brands fa-facebook" size="lg" :style="{ color: 'black' }"/>
                              </a>
                          </li>
                          <li>
                              <a href="#" class="me-4">
                                  <font-awesome-icon icon="fa-brands fa-twitter" size="lg" :style="{ color: 'black' }"/>
                              </a>
                          </li>
                          <li>
                              <a href="#" class="me-4">
                                  <font-awesome-icon icon="fa-brands fa-google" size="lg" :style="{ color: 'black' }"/>
                              </a>
                          </li>
                      </ul>
                     
                  </div> -->
                    <div class="d-flex align-items-center justify-content-center pb-4">
                      <!-- <p class="mb-0 me-2">Don't have an account?</p> <a href="#"> Please Sign Up! </a>
                      <p class="mb-0 me-2">Don't have an account?</p> <a href="#"> Please Sign Up! </a> -->
                      <!-- <button type="button" class="btn btn-outline-danger">Create new</button> -->
                    </div>
                
                  <!-- </form> -->
                
                </div>
              </div>
            </div>
            <div class="col-lg-6 d-flex align-items-center" style="background:#d35400;"> 
              <!-- gradient-custom-2 -->
              <div class="text-white px-3 py-4 p-md-5 mx-md-4">
                <h4 class="mb-4">We are here to change your life...</h4>
                <p class="small mb-0">Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
                  tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud
                  exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
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
    -moz-transition: all .4s ease-in-out;
    -o-transition: all .4s ease-in-out;
    -webkit-transition: all .4s ease-in-out;
    transition: all .4s ease-in-out;
    background-image: linear-gradient(to right, #fc6076, #ff9a44, #ef9d43, #e75516);
    box-shadow: 0 4px 15px 0 rgba(252, 104, 110, 0.75);
}
.auth-btn.invalid {
  animation: shake 0.5s;
  animation-iteration-count: infinite;
}
.btn_signup:hover {
    background-position: 100% 0;
    -moz-transition: all .4s ease-in-out;
    -o-transition: all .4s ease-in-out;
    -webkit-transition: all .4s ease-in-out;
    transition: all .4s ease-in-out;
}

.btn_signup:focus {
    outline: none;
}
</style>