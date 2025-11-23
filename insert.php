<html>
<head>
<title>insert </title>
</head>
<body>
<?php
// Database connection variables
$servername = "localhost";
$username = "root";  // Default username for MySQL
$password = "";      // Default password is empty in XAMPP, WAMP, MAMP
$dbname = "user_db"; // Name of your database
// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
echo "Connected successfully to the database!<br>";
// Query the users table
$sql = "SELECT id, name, email, age FROM users";
$result = $conn->query($sql);
// Check if there are any results
if ($result->num_rows > 0) {
    // Output data of each row
    while($row = $result->fetch_assoc()) {
        echo "ID: " . $row["id"] . " - Name: " . $row["name"] . " - Email: " . $row["email"] . " - Age: " . $row["age"] . "<br>";
    }
} else {
    echo "0 results";
}
// Close the connection
$conn->close();
?>
</body>
</html>