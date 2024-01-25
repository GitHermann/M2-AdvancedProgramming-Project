<template>
  <div class="container">
    <div class="button-row">
      <button class="large-button">Stages</button>
    </div>
    <div class="button-row">
      <button class="small-button">Ajouter un espace de stage</button>
      <button class="small-button">Gérer les espaces de stage</button>
      <button class="small-button">Supprimer un espace de stage</button>
    </div>
  </div>
</template>

<style scoped>

.container {
  margin: 40px;
  margin-top: 150px;
}

.button-row {
  display: flex;
  justify-content: center;
  margin-bottom: 10px;
}

button {
  align-items: center;
  margin-top: 5px;
  margin-bottom: 5px;
  border-radius: 10px;
  width: 50%;
  height: 50px;
  border: solid 1px #c7c4c4;
  font-size: 15px;
  color: #f7f7f7;
  font-family: Verdana, sans-serif;
  font-weight: 800;
  border: solid 1px #c7c4c4;
}

.large-button {
  width: 100%;
  background-color: #3571a9;
}

.small-button {
  background-color: #f7f7f7;
  color: black;
}

</style>
