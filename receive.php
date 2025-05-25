<?php
$data = json_decode(file_get_contents("php://input"), true);
$file = 'data.json';

if ($data && isset($data['id'])) {
    $json = file_exists($file) ? json_decode(file_get_contents($file), true) : [];
    $json[$data['id']] = $data;
    file_put_contents($file, json_encode($json, JSON_PRETTY_PRINT));
    echo "✅ Data saved.";
} else {
    echo "❌ Invalid data.";
}
?>
 
