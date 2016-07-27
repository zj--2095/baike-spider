<?php
session_start();
include_once( 'simple_html_dom.php' );
$keyword=$_GET['keyword'];
$akeyword=urlencode($keyword);
$checkurl='http://baike.baidu.com/item/'.$akeyword;
$checkhtml = file_get_html($checkurl);
foreach($checkhtml->find('h1') as $dom2){;}
$array = (array)$dom2;  
echo is_array($array);
print_r($array);
if (1)
{
	$html = file_get_html($checkurl);

}
else
{
echo '条目';
for($i=0;$i<=10;$i++)
{
	
	$x=$i*10;
	$searchUrl='http://baike.baidu.com/search/none?word='.$akeyword.'&pn='.strval($x).'&rn=10';
	$html = file_get_html($searchUrl);
	foreach($html->find('a[class=result-title]') as $element)
	       {
	       	$result=$element->href . '<br>'; 
	   		$dom = file_get_html($result);
	   		foreach($dom->find('h1') as $dom2){echo $dom2;}
	   		}
}
}
?>