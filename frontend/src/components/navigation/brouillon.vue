</div> <a class="navbar-brand" href="#">LOGO</a>
<!-- <img src="logo.png" alt="Avatar Logo" style="width:40px;" class="rounded-pill">  -->
<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
  <span class="navbar-toggler-icon"></span>
</button>

<div class="collapse navbar-collapse px-4" id="navbarSupportedContent">
  <ul class="navbar-nav mr-auto d-flex justify-content-center">
    <li class="nav-item active">
      <a class="nav-link" href="#">
        <router-link to="/">Home</router-link>
        <span class="sr-only">(current)</span></a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="#">
        <router-link to="/album_detail">About</router-link>
      </a>
    </li>
    <!-- <li class="nav-item dropdown">
      <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
        Dropdown
      </a>
      <div class="dropdown-menu" aria-labelledby="navbarDropdown">
        <a class="dropdown-item" href="#">Action</a>
        <a class="dropdown-item" href="#">Another action</a>
        <div class="dropdown-divider"></div>
        <a class="dropdown-item" href="#">Something else here</a>
      </div>
    </li> -->
    <!-- <li class="nav-item">
      <a class="nav-link disabled" href="#">Disabled</a>
    </li> -->
  </ul>
  <form class="form-inline my-2 my-lg-0">
    <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
    <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
  </form>

  <div class=".col-4 icon_header py-2">
      <!-- Link  to shop -->
      <a href="#">
        <router-link to="/panier">
          <font-awesome-icon icon="fa-solid fa-cart-shopping" size="2x" :style="{ color: 'white' }"/>
          <span class="position-absolute top-0 start-0 translate-middle badge rounded-pill bg-danger">
            99+
          <!-- <span class="visually-hidden">unread messages</span> -->
          </span>
        </router-link>
      </a>
  </div>

  <div class=".col-4 py-2">
      <!-- Link for user  -->
      <a href="#">
        <router-link to="/login">
          <font-awesome-icon icon="fa-solid fa-user" size="2x" :style="{ color: 'white' }"/>
        </router-link>
        
      </a>
  </div>
  
</div>

<!-- <Wizard
        squared-tabs
        card-background
        navigable-tabs
        scrollable-tabs
        :nextButton="{
          text: 'Next',
          icon: 'check',
          hideIcon: true, // default false but selected for sample
          hideText: false, // default false but selected for sample
        }"
        :custom-tabs="[
          {
            title: 'Shopping',
          },
          {
            title: 'Authentification',
          },
          {
            title: 'Livraison',
          },
          {
            title: 'Paiement',
          },
          {
            title: 'Terminee',
          },
        ]"
        :beforeChange="onTabBeforeChange"
        @change="onChangeCurrentTab"
        @complete:wizard="wizardCompleted"
      > -->

      // import Wizard from 'form-wizard-vue3';

// export default {
//   components: {
//     Wizard,
//     Liste_Commandes,
//   } , 
//   data() {
//     return {
//       currentTabIndex: 0,
//     };
//   },
//   methods: {
//     onChangeCurrentTab(index:any, oldIndex:any) {
//       console.log(index, oldIndex);
//       this.currentTabIndex = index;
//     },
//     onTabBeforeChange() {
//       if (this.currentTabIndex === 0) {
//         console.log('First Tab');
//       }
//       console.log('All Tabs');
//     },
//     wizardCompleted() {
//       console.log('Wizard Completed');
//     },
//   },
// };

// import 'form-wizard-vue3/dist/form-wizard-vue3.css';