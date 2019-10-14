<?php
$path = strip_tags($_GET['file']);
header("Cache-Control: no-store, no-cache,must-revalidate");
header("Cache-Control: post-check=0, pre-check=0", false);
header("Pragma: no-cache");
header('Content-Length: ' . filesize("media/4c2e5b52-a323-4ac4-8be3-7ee059439e55/" . $path));
header('Content-type:application/force-download');
if (strpos($_GET['file'], ".ts") > 1) header("Content-type: video/MP2T");
if (strpos($_GET['file'], ".m3u8") > 1) header("Content-type: application/x-mpegURL");
@readfile("media/4c2e5b52-a323-4ac4-8be3-7ee059439e55/" . $path);
