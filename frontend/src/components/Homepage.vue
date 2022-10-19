<script>
  import { MDBListGroup, MDBListGroupItem } from "mdb-vue-ui-kit";
  export default {
    components: {
      MDBListGroup,
      MDBListGroupItem
    }
  };
</script>


<template>
        
        <h1>Listes des categories </h1>
          <MDBListGroup light class=".me-3">
                <MDBListGroupItem>Categorie 1</MDBListGroupItem>
                <MDBListGroupItem>Categorie 2</MDBListGroupItem>
                <MDBListGroupItem>Categorie 3</MDBListGroupItem>
                <MDBListGroupItem>Categorie 4</MDBListGroupItem>
                <MDBListGroupItem>Categorie 5</MDBListGroupItem>
          </MDBListGroup>
       
        <hr class="hr" />
        <h1>Liste des albums </h1>
        <MDBListGroup>
                <MDBListGroupItem>Album 1</MDBListGroupItem>
                <MDBListGroupItem>Album 2</MDBListGroupItem>
                <MDBListGroupItem>Album 3</MDBListGroupItem>
                <MDBListGroupItem>Album 4</MDBListGroupItem>
                <MDBListGroupItem>Album 5</MDBListGroupItem>
        </MDBListGroup>
        
        
</template>
<style scoped>
        h1 {
                padding-top: 50px;
        }
        template {
                margin-top: 100px;
                margin-bottom: 100px;
                margin-right: 150px;
                margin-left: 80px;
        }
</style>