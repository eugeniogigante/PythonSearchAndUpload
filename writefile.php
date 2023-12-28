<?php
if ($_FILES['file']['error'] === UPLOAD_ERR_OK) {
    $tempFile = $_FILES['file']['tmp_name'];
    $targetPath = 'uploads/';
    $targetFile = $targetPath . basename($_FILES['file']['name']);
    move_uploaded_file($tempFile, $targetFile);
    echo "File uploaded successfully!";
} else {
    echo "File upload failed.";
}
?>
