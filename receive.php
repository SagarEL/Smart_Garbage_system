<?php
// Set CORS header (optional, useful if webpage reads this data too)
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json");

// Read the raw POST data
$json = file_get_contents('php://input');
$data = json_decode($json, true);

// Validate required fields
if (isset($data['id']) && isset($data['level']) && isset($data['lat']) && isset($data['lng'])) {
    $id = $data['id'];
    $level = $data['level'];
    $lat = $data['lat'];
    $lng = $data['lng'];
    $timestamp = date("Y-m-d H:i:s");

    // Save to file (or later, to database)
    $entry = "$timestamp - ID: $id, Level: $level%, Location: $lat,$lng\n";
    file_put_contents("dustbin_log.txt", $entry, FILE_APPEND);

    echo json_encode(["status" => "success", "message" => "Data received", "data" => $data]);
} else {
    echo json_encode(["status" => "error", "message" => "Invalid JSON data"]);
}
