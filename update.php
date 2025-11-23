
<!DOCTYPE html>
<html>
<head>
    <title>Update Record</title>
</head>
<body>
<?php
// Database connection variables
$servername = "localhost";
$username = "root";   
$password = "";       
$dbname = "user_db";   // <-- updated database name

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Update Bob Smith's age
$sql = "UPDATE users SET age = 32 WHERE name = 'Bob Smith'";

if ($conn->query($sql) === TRUE) {
    echo "Record updated successfully!<br>";
} else {
    echo "Error updating record: " . $conn->error . "<br>";
}

// Close the connection
$conn->close();
?>
</body>
</html>