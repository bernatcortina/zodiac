<html>
<head>
    <title>${projecte}</title>
</head>
<body>
    <h1>${projecte}</h1>
    <p>
    	% for foto in imatges:
			<img src="/static/fotos_zodiac/${foto}" width="100" height="100" alt="${foto}"/>
    	% endfor
    </p>

    <p>
    	<a href="${request.route_url('entra_dades')}">CONEIX EL TEU SIGNE</a>
    </p>

</body>
</html>
