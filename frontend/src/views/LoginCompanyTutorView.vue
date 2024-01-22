<template>
    <div class="container">
        <form class="login-form" @submit="login">
            <div>
                <h2 class="title">Connexion</h2>
            </div>
            <label class="text" for="username">Nom d'utilisateur :</label>
            <input v-model="username" type="text" id="username" name="username" class="input-form" required>

            <label class="text" for="password">Mot de passe :</label>
            <input v-model="password" type="password" id="password" name="password" class="input-form" required>

            <button class="submit-button" type="submit">Se connecter</button>
        </form>
    </div>
</template>

<script>
export default {
    data() {
        return {
            username: '',
            password: ''
        };
    },
    methods: {
        login(event) {
            event.preventDefault();
           
            console.log('Username:', this.username);
            console.log('Password:', this.password);
            
            this.username = '';
            this.password = '';
        }
    }
}
</script>

<style scoped>
.container {
    margin: 0 auto;
    margin-top: 50px;
    width: 600px;
    display: flex;
    flex-direction: column;
    align-items: center;
    
}

.login-form {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 10px;
    margin: 10px;
    background-color: #f0f0f0;
    border: none;
    border-radius: 10px;
    width: 90%;
    box-shadow: 2px 2px 2px rgba(0, 0, 0, 0.2); 
}


.input-form {
    display: flex;
    align-items: center;
    padding: 10px;
    margin-top: 20px;
    margin-bottom: 20px;
    background-color: #f7f7f7;
    border-radius: 10px;
    width: 80%;
    height: 32px;
    border: solid 1px #c7c4c4;
}

.submit-button {
    align-items: center;
    margin-top: 20px;
    margin-bottom: 20px;
    background-color: #3571a9;
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

.title {
    font-size: 25px;
    font-family: Verdana, sans-serif;
    margin-bottom: 40px;
}

.text {
    font-size: 16px;
    font-family: Verdana, sans-serif;
}

</style>
