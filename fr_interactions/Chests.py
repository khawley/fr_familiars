# data includes id of chest, and ver=conn, the 'confirmed' click to open
# page= not needed for it to work


# iron treasure chest - which id #575
"""
curl 'http://flightrising.com/includes/ol/openchest.php' -H 'Cookie: PHPSESSID=test' -H 'Origin: http://flightrising.com' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: en-US,en;q=0.8' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36' -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H 'Accept: */*' -H 'Referer: http://flightrising.com/main.php?p=hoard&tab=other&page=2' -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive' --data 'id=575&ver=con&page=2' --compressed
"""



"""
        <div style="text-align:left; margin-bottom:15px; font-size:11px;">You found the following items:</div>
		<div style="width:475px; margin-left:auto; margin-right:auto; text-align:center;">

					<span style="width:85px; position:relative; display:inline-block;">
				<a rel="includes/itemajax.php?id=208&tab=trinket" class="clue">
					<img src="/images/cms/trinket/208.png" />
					<div style="font-size:12px; color:#731d08; font-weight:bold;">
					2					</div>
				</a>
			</span>
						<span style="width:85px; position:relative; display:inline-block;">
				<a rel="includes/itemajax.php?id=6349&tab=trinket" class="clue">
					<img src="/images/cms/trinket/6349.png" />
					<div style="font-size:12px; color:#731d08; font-weight:bold;">
					4					</div>
				</a>
			</span>
						<span style="width:85px; position:relative; display:inline-block;">
				<a rel="includes/itemajax.php?id=283&tab=equipment" class="clue">
					<img src="/images/cms/equipment/283.png" />
					<div style="font-size:12px; color:#731d08; font-weight:bold;">
					1					</div>
				</a>
			</span>
						<span style="width:85px; position:relative; display:inline-block;">
				<img src="/images/layout/treasure_pile.png" />
				<div style="font-size:12px; color:#731d08; font-weight:bold;">
				4110				</div>
			</span>
						<span style="width:85px; position:relative; display:inline-block;">
				<img src="/images/layout/gem_pile.png" width="85" height="85" />
				<div style="font-size:12px; color:#731d08; font-weight:bold;">
				5				</div>
			</span>
					</div>
		<div style="margin-top:15px; text-align:center; margin-bottom:10px;">
			<button class="beigebutton thingbutton" id="no">Collect</button>
		</div>
        	<script type="text/javascript">
	$(function(){
		$('#no').click(function(e){
			window.location ='main.php?p=hoard&tab=other&page=2';
			$("#specialty").html('<img src="/images/layout/loading.gif"> loading...');
		});
	});
	$('a.clue').cluetip({
		height:"auto"
	});
	</script>
"""


# rusted treasure chest #574
"""curl 'http://flightrising.com/includes/ol/openchest.php' -H 'Cookie: PHPSESSID=test' -H 'Origin: http://flightrising.com' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: en-US,en;q=0.8' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36' -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H 'Accept: */*' -H 'Referer: http://flightrising.com/main.php?p=hoard&tab=other&page=2' -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive' --data 'id=574&ver=con&page=2' --compressed"""

"""
        <div style="text-align:left; margin-bottom:15px; font-size:11px;">You found the following items:</div>
		<div style="width:475px; margin-left:auto; margin-right:auto; text-align:center;">

					<span style="width:85px; position:relative; display:inline-block;">
				<a rel="includes/itemajax.php?id=1161&tab=trinket" class="clue">
					<img src="/images/cms/trinket/1161.png" />
					<div style="font-size:12px; color:#731d08; font-weight:bold;">
					2					</div>
				</a>
			</span>
						<span style="width:85px; position:relative; display:inline-block;">
				<a rel="includes/itemajax.php?id=3538&tab=equipment" class="clue">
					<img src="/images/cms/equipment/3538.png" />
					<div style="font-size:12px; color:#731d08; font-weight:bold;">
					1					</div>
				</a>
			</span>
						<span style="width:85px; position:relative; display:inline-block;">
				<a rel="includes/itemajax.php?id=7889&tab=trinket" class="clue">
					<img src="/images/cms/trinket/7889.png" />
					<div style="font-size:12px; color:#731d08; font-weight:bold;">
					1					</div>
				</a>
			</span>
						<span style="width:85px; position:relative; display:inline-block;">
				<img src="/images/layout/treasure_pile.png" />
				<div style="font-size:12px; color:#731d08; font-weight:bold;">
				1775				</div>
			</span>
					</div>
		<div style="margin-top:15px; text-align:center; margin-bottom:10px;">
			<button class="beigebutton thingbutton" id="no">Collect</button>
		</div>
        	<script type="text/javascript">
	$(function(){
		$('#no').click(function(e){
			window.location ='main.php?p=hoard&tab=other&page=2';
			$("#specialty").html('<img src="/images/layout/loading.gif"> loading...');
		});
	});
	$('a.clue').cluetip({
		height:"auto"
	});
	</script>
"""