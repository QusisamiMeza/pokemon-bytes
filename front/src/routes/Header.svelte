<header>
    <div class="presentacion_pag">
        <img class="img_izq" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/International_Pok%C3%A9mon_logo.svg/1024px-International_Pok%C3%A9mon_logo.svg.png" alt="https://i.pinimg.com/originals/44/0c/c2/440cc2c2f4abd45f1f563a7165fb6344.png"/>
        <h1>Pokémon Bytes</h1>
        <img class="img_der" src="https://i.pinimg.com/originals/8a/2a/73/8a2a73c4e85a9efc11a230e285a0db53.png" alt="https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Pokebola-pokeball-png-0.png/640px-Pokebola-pokeball-png-0.png"/>
    </div>
    <nav><a class=nav-button href="/"><b>HOME</b></a>
        <a class=nav-button href="/pokemons"><b>POKEMONS</b></a>
        <a class=nav-button href="/moves"><b>MOVES</b></a>
        <a class=nav-button href="/teams"><b>TEAMS</b></a>
    </nav>
</header>

<style>
    .presentacion_pag {
        background-color: #252525;
        height: 100px;
        text-align: center;
        justify-content: space-around;
        align-items: center;
        display: flex;
        color: #20B0ED;
        font-family: "Press Start 2P", system-ui;
        font-size: 24px;
        letter-spacing: 2px;
        border-top: #404040 solid 3px;
    }

    .presentacion_pag .img_izq {
        width: 240px;
        height: 100px;
    }

    .presentacion_pag .img_der {
        width: 113px;
        height: 95px;
    }

    nav {
		display: flex;
		justify-content: space-around;
        font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
        font-size: 15px;
        background-color: #404040;
        border-top: #e41d1a solid 2px;
	}

    .nav-button {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 200px;
        height: 40px;
        color: rgb(177, 177, 177);
    }

    .nav-button:hover {
        background-color: #e41d1a;
        color: #ffffff;
    }

    nav img {
        width: 105px;
        height: 32px;
        margin-top: 4px;
        margin-bottom: 4px;
        margin-left: 20px;
    }
</style>