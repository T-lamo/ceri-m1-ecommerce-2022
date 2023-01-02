<script lang="ts" setup>
  import { decodeCredential , googleLogout} from 'vue3-google-login';

  const callback = (response:any) => {
    const userData = decodeCredential(response.credential)
    console.log("Handle the userData", userData)
  }


  const logout_my_account = () => {
    googleLogout()
    console.log("logging out")
    
  }
</script>
<template>
    <div>
        <GoogleLogin :callback="callback" prompt/>
        <p> Bonjour login </p>
        <button class="g_id_signout" @click="logout_my_account">LogOut</button>
    </div>
    
</template>
