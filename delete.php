<!DOCTYPE html>
<html>
<head>
    <title>Delete Record</title>
</head>
<body>
<?php
// Database connection variables
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "user_db";   // <-- your database name

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Delete Charlie Brown (id = 3)
$sql = "DELETE FROM users WHERE id = 3";

if ($conn->query($sql) === TRUE) {
    echo "<p style='color:green;'>Record deleted successfully!</p>";
} else {
    echo "<p style='color:red;'>Error deleting record: " . $conn->error . "</p>";
}

// Close the connection
$conn->close();
?>
</body>
</html>