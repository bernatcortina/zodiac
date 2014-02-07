<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="Content-type" content="text/html; charset=utf-8">
    <title>${projecte}</title>
    <style>
        td {
            border: 1px solid black;
        }
    </style>
</head>
<body>
    <h1>${projecte}</h1>

    <table>
        <tr>
            <th>Data</th>
            <th>Signe</th>
            <th>Frase</th>
        </tr>
    % for guest in guestbook:
        <tr>
            <td>${guest.date}</td>
            <td>${guest.signe}</td>
            <td>${guest.frase}</td>
        </tr>
    % endfor
    </table>


</body>
</html>
