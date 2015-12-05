
class CurlPetFamiliarResponses(object):

    @classmethod
    def respond_gold_chest(cls, *args, **kwargs):
        return cls.gold_chest_response

    @classmethod
    def respond_iron_chest(cls, *args, **kwargs):
        return cls.iron_chest_response

    @classmethod
    def respond_rusted_chest(cls, *args, **kwargs):
        return cls.rusted_chest_response

    @classmethod
    def respond_treasure_only(cls, *args, **kwargs):
        return cls.treasure_only_response

    @classmethod
    def respond_gem(cls, *args, **kwargs):
        return cls.gem_response

    # need to get a sample html
    gem_response = """ """

    gold_chest_response = """
        <script type="text/javascript">
$(function(){
	$('#no').click(function(e){
		window.location.reload();
	});
});
</script>

			<script type="text/javascript">
			$('a.clue').cluetip({
				height:"auto"
			});
			</script>

			<div style="height:220px; width:410px; margin-bottom:15px;">

			<span style="height:200px; width:200px; display:inline-block; background-color:#EEE; border:1px solid #BBB; margin-right:15px; vertical-align:top;">
			<img src="/images/cms/familiar/art/6338.png" border="0" />
			</span>

			<span style="width:185px; height:200px; display:inline-block; vertical-align:top;">
				<div style="margin-bottom:10px;">
				Your <span style="font-weight:bold; color:#731d08;">Familiar</span> has <span style="font-weight:bold; color:#731d08;">awakened</span> its true potential and is aglow with enthusiasm.<br />
				<br />
				Visit <span style="font-weight:bold;">once each day</span> to bond with it and earn rewards!<br />
				<br />
				You've earned these rewards today:
				</div>
				<div style="text-align:center; font-weight:bold; size:#731d08;">
					<span style="width:85px; height:100px; text-align:center; display:inline-block;">
					<img src="/images/layout/treasure_pile.png" border="0" />
					50					</span>
											<span style="width:85px; height:100px; text-align:center; display:inline-block; margin-left:10px;">
						<a rel="includes/itemajax.php?id=576&tab=trinket" class="clue"><img src="/images/cms/trinket/576.png" border="0" /></a>
						1						</span>
										</div>
			</span>

			</div>


			<div style="margin-top:15px; text-align:center; margin-bottom:10px;">
			<button class="beigebutton thingbutton" id="no">Okay</button>
			</div>

"""

    iron_chest_response = """
    <script type="text/javascript">
$(function(){
	$('#no').click(function(e){
		window.location.reload();
	});
});
</script>

			<script type="text/javascript">
			$('a.clue').cluetip({
				height:"auto"
			});
			</script>

			<div style="height:220px; width:410px; margin-bottom:15px;">

			<span style="height:200px; width:200px; display:inline-block; background-color:#EEE; border:1px solid #BBB; margin-right:15px; vertical-align:top;">
			<img src="/images/cms/familiar/art/6338.png" border="0" />
			</span>

			<span style="width:185px; height:200px; display:inline-block; vertical-align:top;">
				<div style="margin-bottom:10px;">
				Your <span style="font-weight:bold; color:#731d08;">Familiar</span> is a stalwart <span style="font-weight:bold; color:#731d08;">companion</span>; you go everywhere together!<br />
				<br />
				Visit <span style="font-weight:bold;">once each day</span> to bond with it and earn rewards!<br />
				<br />
				You've earned these rewards today:
				</div>
				<div style="text-align:center; font-weight:bold; size:#731d08;">
					<span style="width:85px; height:100px; text-align:center; display:inline-block;">
					<img src="/images/layout/treasure_pile.png" border="0" />
					35					</span>
											<span style="width:85px; height:100px; text-align:center; display:inline-block; margin-left:10px;">
						<a rel="includes/itemajax.php?id=575&tab=trinket" class="clue"><img src="/images/cms/trinket/575.png" border="0" /></a>
						1						</span>
										</div>
			</span>

			</div>


			<div style="margin-top:15px; text-align:center; margin-bottom:10px;">
			<button class="beigebutton thingbutton" id="no">Okay</button>
			</div>

"""

    rusted_chest_response = """
        <script type="text/javascript">
$(function(){
	$('#no').click(function(e){
		window.location.reload();
	});
});
</script>

			<script type="text/javascript">
			$('a.clue').cluetip({
				height:"auto"
			});
			</script>

			<div style="height:220px; width:410px; margin-bottom:15px;">

			<span style="height:200px; width:200px; display:inline-block; background-color:#EEE; border:1px solid #BBB; margin-right:15px; vertical-align:top;">
			<img src="/images/cms/familiar/art/6338.png" border="0" />
			</span>

			<span style="width:185px; height:200px; display:inline-block; vertical-align:top;">
				<div style="margin-bottom:10px;">
				Your <span style="font-weight:bold; color:#731d08;">Familiar</span> is <span style="font-weight:bold; color:#731d08;">tolerant</span> of you, but it seems to be warming up slightly.<br />
				<br />
				Visit <span style="font-weight:bold;">once each day</span> to bond with it and earn rewards!<br />
				<br />
				You've earned these rewards today:
				</div>
				<div style="text-align:center; font-weight:bold; size:#731d08;">
					<span style="width:85px; height:100px; text-align:center; display:inline-block;">
					<img src="/images/layout/treasure_pile.png" border="0" />
					20					</span>
											<span style="width:85px; height:100px; text-align:center; display:inline-block; margin-left:10px;">
						<a rel="includes/itemajax.php?id=574&tab=trinket" class="clue"><img src="/images/cms/trinket/574.png" border="0" /></a>
						1						</span>
										</div>
			</span>

			</div>


			<div style="margin-top:15px; text-align:center; margin-bottom:10px;">
			<button class="beigebutton thingbutton" id="no">Okay</button>
			</div>

"""

    treasure_only_response = """
    <script type="text/javascript">
$(function(){
	$('#no').click(function(e){
		window.location.reload();
	});
});
</script>

			<script type="text/javascript">
			$('a.clue').cluetip({
				height:"auto"
			});
			</script>

			<div style="height:220px; width:410px; margin-bottom:15px;">

			<span style="height:200px; width:200px; display:inline-block; background-color:#EEE; border:1px solid #BBB; margin-right:15px; vertical-align:top;">
			<img src="/images/cms/familiar/art/611.png" border="0" />
			</span>

			<span style="width:185px; height:200px; display:inline-block; vertical-align:top;">
				<div style="margin-bottom:10px;">
				Your <span style="font-weight:bold; color:#731d08;">Gale Wolf</span> is <span style="font-weight:bold; color:#731d08;">inquisitive</span> and wants to learn more about your clan.<br />
				<br />
				Visit <span style="font-weight:bold;">once each day</span> to bond with it and earn rewards!<br />
				<br />
				You've earned these rewards today:
				</div>
				<div style="text-align:center; font-weight:bold; size:#731d08;">
					<span style="width:85px; height:100px; text-align:center; display:inline-block;">
					<img src="/images/layout/treasure_pile.png" border="0" />
					30					</span>
									</div>
			</span>

			</div>


			<div style="margin-top:15px; text-align:center; margin-bottom:10px;">
			<button class="beigebutton thingbutton" id="no">Okay</button>
			</div>
"""
