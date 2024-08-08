<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ninja Town</title>
  <link rel="stylesheet" href="/public/styles.css">
</head>
<body>
  <h1>Welcome to Ninja Town</h1>
  <ul>
    % for ninja in ninjas:
    <li>
      <div>{{ninja['name']}} - {{ninja['belt_color']}} belt</div>
      <div>Special move - {{ninja['special_move']}}</div>
    </li>
    % end
  </ul>
</body>
</html>