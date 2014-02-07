<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="Content-type" content="text/html; charset=utf-8">
    <title>${projecte}</title>
</head>
<body>
    <h1>Formulari ${projecte}</h1>
    <p>
    	<form method="POST">
            Nom:<br>
            <input type="text" name="nom" /><br>
            Data naixement:<br>
            <select name="dia_naix">
                <option value="1">01</option>
                <option value="2">02</option>
                <option value="3">03</option>
                <option value="4">04</option>
                <option value="5">05</option>
                <option value="6">06</option>
                <option value="7">07</option>
                <option value="8">08</option>
                <option value="9">09</option>
                <option value="10">10</option>
                <option value="11">11</option>
                <option value="12">12</option>
                <option value="13">13</option>
                <option value="14">14</option>
                <option value="15">15</option>
                <option value="16">16</option>
                <option value="17">17</option>
                <option value="18">18</option>
                <option value="19">19</option>
                <option value="20">20</option>
                <option value="21">21</option>
                <option value="22">22</option>
                <option value="23">23</option>
                <option value="24">24</option>
                <option value="25">25</option>
                <option value="26">26</option>
                <option value="27">27</option>
                <option value="28">28</option>
                <option value="29">29</option>
                <option value="30">30</option>
                <option value="31">31</option>
            </select>
            <select name="mes_naix">
                <option value="1">Gener</option>
                <option value="2">Febrer</option>
                <option value="3">Març</option>
                <option value="4">Abril</option>
                <option value="5">Maig</option>
                <option value="6">Juny</option>
                <option value="7">Juliol</option>
                <option value="8">Agost</option>
                <option value="9">Setembre</option>
                <option value="10">Octubre</option>
                <option value="11">Novembre</option>
                <option value="12">Desembre</option>
            </select>
            <br><br>
            Vols guardar la visita al llibre de visites?<br>
            <select name="terms">
                <option value="si" selected>Si</option>
                <option value="no">No</option>
            </select>
            <br><br>
            <input type="submit" value="Envia">
        </form>
    </p>

    % if missatge:
        <p>${nom}, el teu signe és: ${signe} </p>
        <p>
            <img src="/static/fotos_zodiac/${imatge}" width="100" height="100" alt="${imatge}"/>
        </p>
        <p>Missatge de la fortuna: ${missatge} </p>
        <p>
            <a href="/">TORNA A L'INICI</a>
        </p>
        <p>
            <a href="${request.route_url('guest_book')}">MIRA EL LLIBRE DE VISITES</a>
        </p>
    % endif




</body>
</html>
