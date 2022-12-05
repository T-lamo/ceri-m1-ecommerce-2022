<script lang="ts" setup>
    import { ref,onMounted } from "vue"
    import { User } from "@/models";
    import { create_user,read_users } from "@/services/crud";
    import { useAppStore } from "@/stores";
    import { storeToRefs } from "pinia";

    const { list_category , list_users} = storeToRefs(useAppStore())
    onMounted(async () => {
      list_users.value = (await read_users()).map((res:any) => {
        console.log(res)
            return res;
        })
    })

    const show = ref(true)

    const toggle = () => {
        show.value = !show.value
    }

    let passwordcheck = ref('')

    let user = {
      username:ref(''),
      firstname:ref(''),
      email:ref(''),
      password:ref(''),
      is_admin: false
    }
   
    const addUser = async () => {
      console.log("my_user")
      console.log(user.username.value)
      const response = await create_user(new User({
        "username":user.username.value,
        "firstname":user.firstname.value,
        "email":user.email.value,
        "password":user.password.value,
        "is_admin": user.is_admin}))
            .then(res =>  console.log(res) )
            .catch(error => console.log(error))
          
    }
</script>
<template>
<section class="mb-5" style="background-color:transparent;">
  <!-- gradient-form -->
  <div class="container py-5 h-80">
    <div class="row d-flex justify-content-center align-items-center h-80">
      <div class="col-xl-10">
        <div class="card rounded-3 text-black">
          <div class="row"> <!-- g-0-->
            <div class="col-lg-6">
              <div class="card-body p-md-5 mx-md-4">

                <div class="text-center">
                  <!-- <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS50it_iEXGxpPgB0YfjZGlsXcm0SzZlEWcpA&usqp=CAU"
                    style="width: 185px;" alt="logo"> -->
                  <h4 v-if="show" class="mt-1 mb-5 pb-1">Log In </h4>
                  <h4 v-else class="mt-1 mb-5 pb-1 ">Sign Up </h4>
                </div>

                <form>
                  <!-- <p>Please login to your account</p> -->
                <div v-if="show">
                    <div class="form-floating mb-3">
                        <input type="email" class="form-control" id="floatingInput" placeholder="name@example.com">
                        <label for="floatingInput">Email address</label>
                      </div>
                      <!-- <label>Validate me </label> -->

                    <div class="form-floating mb-3">
                        <input type="password" id="floatingpasswordinput" class="form-control" placeholder="...type your password here"/>
                        <label for="floatingpasswordinput">Password</label>
                    </div>
                    
                    <div class="text-center pt-1 mb-5 pb-1">
                        <button class="btn btn-outline-warning btn-block mb-3" type="button">
                          <!-- gradient-custom-2 -->
                          Log in
                        </button> <br>
                        <a class="text-muted text-center" href="#!">Forgot password?</a>
                    </div>
                </div>
                   <!-- Please sign up -->
                <div v-else>
                  {{user}}
                    <div class="form-floating mb-3">
                            <input type="text" class="form-control" id="floatingUsernameInput" placeholder="name@example.com" v-model="user.username.value">
                            <label for="floatingUsernameInput">Username</label>
                        </div>
                        <div class="form-floating mb-3">
                            <input type="text" class="form-control" id="floatingfirstnameInput" placeholder="name@example.com" v-model="user.firstname.value">
                            <label for="floatingfirstnameInput">Firstname</label>
                        </div>
                        <div class="form-floating mb-3">
                            <input type="email" class="form-control" id="floatingemailInput" placeholder="name@example.com" v-model="user.email.value">
                            <label for="floatingemailInput">Email address</label>
                        </div>

                    <div class="form-floating mb-3">
                        <input type="password" id="floatingpasswordinput1" class="form-control" placeholder="...type your password here" v-model="user.password.value">
                        <label for="floatingpasswordinput1">Password</label>
                    </div>
                    <div class="form-floating mb-3">
                        <input type="password" id="floatingpasswordinput2" class="form-control" placeholder="...retype your password here" v-model="passwordcheck">
                        <label for="floatingpasswordinput2">Repeat Password</label>
                    </div>
                      
                  <div class="text-center pt-1 mb-5 pb-1">
                    <button class="btn btn-outline-warning btn-block" type="button" @click="addUser()">
                        Sign Up
                    </button>
                    <!-- <a class="text-muted" href="#!">Forgot password?</a> -->
                </div>
            </div>
                <p class="text-center" v-if="show">Or Log in with:</p>
                <p class="text-center" v-else>Or Sign Up with:</p>
                <!-- list of icons to log in social media -->
                <div class="d-flex align-items-center justify-content-center pb-4">
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
                   
                </div>
                  <div class="d-flex align-items-center justify-content-center pb-4">
                    <!-- <p class="mb-0 me-2">Don't have an account?</p> <a href="#"> Please Sign Up! </a>
                    <p class="mb-0 me-2">Don't have an account?</p> <a href="#"> Please Sign Up! </a> -->
                    <!-- <button type="button" class="btn btn-outline-danger">Create new</button> -->
                  </div>

                </form>

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
  .gradient-custom-2 {

/* fallback for old browsers */
background: #fccb90;

/* Chrome 10-25, Safari 5.1-6 */
background: -webkit-linear-gradient(to right, #ee7724, #d8363a, #dd3675, #b44593);

/* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
background: linear-gradient(to right, #ee7724, #d8363a, #dd3675, #b44593);
}

@media (min-width: 768px) {
.gradient-form {
height: 100vh !important;
}
}
@media (min-width: 769px) {
.gradient-custom-2 {
border-top-right-radius: .3rem;
border-bottom-right-radius: .3rem;
}
}
</style>