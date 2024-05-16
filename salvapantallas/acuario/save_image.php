<?php

function getEpochMilliseconds() {
    // Get the current Unix timestamp with microseconds
    $microtime = microtime(true);
    
    // Convert the timestamp to milliseconds
    $milliseconds = round($microtime * 1000);
    
    return $milliseconds;
}

if (isset($_POST['imgData'])) {
    $imgData = $_POST['imgData'];

    // Remove the "data:image/jpeg;base64," part
    $imgData = str_replace('data:image/jpeg;base64,', '', $imgData);
    $imgData = str_replace(' ', '+', $imgData);

    // Decode the base64 encoded data
    $data = base64_decode($imgData);

    // Specify the file path where the image will be saved
    $filePath = 'render/img'.sprintf('%013d', $_POST['fotograma']).'.jpg';

    // Save the image
    file_put_contents($filePath, $data);

    echo 'Image saved successfully!';
} else {
    echo 'No image data received!';
}
?>