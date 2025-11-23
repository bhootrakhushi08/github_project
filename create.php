<!DOCTYPE html>
<html>
<head>
    <title>Fetch Users</title>
</head>
<body>
<?php
// Database connection variables
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "khushi";  // your database name

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// SQL query to fetch data
$sql = "SELECT id, name FROM k1";  
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // Output data of each row
    while($row = $result->fetch_assoc()) {
        echo "ID: " . $row["id"]. " - Name: " . $row["name"]. "<br>";
    }
} else {
    echo "0 results";
}

// Close connection
$conn->close();
?>
</body>
</html>
