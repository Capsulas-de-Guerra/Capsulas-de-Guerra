<template>
  <div id="app">
    <img class="logo" src="./assets/logo.png" />

    <div class="inbox-login">
      <table>
        <tr>
          <td>
            <label> Usuário</label>
          </td>
          <td>
            <input class="input-login" type="text" />
          </td>
        </tr>
        <tr>
          <td>
            <label> Senha</label>
          </td>
          <td>
            <input class="input-login" type="password" />
          </td>
        </tr>
      </table>
    </div>
   
    <input class="btn-login" type="submit" value="Entrar" />
    <a :href=" link "><input type="submit" class="btn-cadastro" value="Cadastrar" /></a>
  </div>
</template>

<script>

export default {
  name: "app",
  data() {

    
    return {
      msg: "Welcome to Your Vue.js App",
      link: "https://www.google.com",
    };
  },

};
</script>

<style lang="scss">
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  align-items: center;
  align-self: auto;
  text-align: center;
  color: #03A688;
  margin-top: 60px;
  width: 23%;
  box-shadow: 8px 5px 5px rgb(76, 75, 75);

  border-radius: 15px;
  background-color: rgb(255, 255, 255);
  padding-top: 30px;
  padding-bottom: 30px;
}

.btn-login {
  color: white;
  background-color: #03A688;
  border-radius: 5px;
  width: 80px;
  height: 35px;
}
.btn-cadastro {
  color: white;
  background-color: #048ABF;
  border-radius: 5px;
  width: 80px;
  height: 35px;
}

.inbox-login {
  margin-inline-start: 68px;
}

.logo {
  width: 200px;
}
h1,
h2 {
  font-weight: normal;
  text-align: center;
}

input {
  margin: 5px;
}

.input-login {
  border-bottom-style: groove;
  border-top-style: hidden;
  border-left-style: hidden;
  border-right-style: hidden;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color:#038C0C;
}

body {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  background-color: #0583F2;
}
</style>
