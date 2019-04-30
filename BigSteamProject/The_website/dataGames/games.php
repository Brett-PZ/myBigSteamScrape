
<?php
$category=$_POST['category'];
if ($category == NULL) {
  $category = "id";
}
include 'database.php';
$query= "SELECT * FROM games ORDER BY $category ASC ";
$intro= mysqli_query($conn, $query);


 ?>

 <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name=viewport content="width=device-width, initial-scale=1">
    <Title>Top 100 Steam Games</title>
      <link rel="stylesheet" href="css/main.css">
      <link rel ="stylesheet" href="css/table.css">
      <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
      <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
    </head>

    <body>
      <div id="container">
      <h1>Top 100 Steam Games</h1>

      <h2>Need help finding a game? Narrow your search. </h2>
          <form action="games.php" method="post">
             <fieldset>
                <legend>Search by Rank, Price, Details, or Genre.</legend>
                <p>
                   <label>Select list</label>
                   <select name="category" id="category">
                     <option value="id">Rank</option>
                     <option value="price">Price</option>
                     <option value="details">Details</option>
                     <option value="genre">Genre</option>
                   </select>
                </p>
             </fieldset>
             <input type="submit">
          </form>
 <table class="pure-table">
   <tr>
     <th>Rank</th>
     <th>Link</th>
     <th>Price</th>
     <th>Title</th>
     <th>Details</th>
     <th>Genre</th>
   </tr>
<tr>
<?php while ($row = mysqli_fetch_assoc($intro)) : ?>


    <td><?php echo $row['id'];?></td>
    <td><?php echo $row['urls'];?></td>
    <td><?php echo $row['price'];?></td>
    <td><?php echo $row['title'];?></td>
    <td><?php echo $row['details'];?></td>
    <td><?php echo $row['genre'];?></td>
  </tr>
<?php endwhile; ?>
</table>

<footer>
  <button type="button"><a href="https://github.com/Brett-PZ/myBigSteamScrape/">Click here for my github page.</a></button>
</body>
</html>
