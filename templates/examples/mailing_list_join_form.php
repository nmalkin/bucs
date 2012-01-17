<h1>Request further information</h1>
<p>The BUCS secretariat is hard at work preparing for the conference. As
	more information becomes available, it will be posted on our website.</p>
<p>
	If you may be interested in the conference, please consider joining our
	mailing list. We will use it to inform you of major changes and
	additions (for example, when the topics and committees appear on the
	website). This is a very low-traffic list (expect one message every few
	months), and we will <em>only</em> use your contact information to send
	you updates about the Brown University Crisis Simulation.
</p>
<p>To join our mailing list, fill out the form below:</p>


<?php
echo form_open('mailing_list/join');
echo validation_errors('<div class="error" style="margin-left:10px">', '</div>');
?>
<p>
	What is your name?<br /> <input type="text" name="name" />
</p>
<p>
	What is the name of your school?<br /> <input type="text" name="school" />
</p>
<p>
	What is your contact e-mail address?<br /> <input type="text"
		name="email" />
</p>
<p>
	What is your best estimate of the number of delegates you will be
	sending to BUCS?<br /> <input type="number" name="delegates" />
</p>
<p>How did you hear about BUCS?</p>
<ul style="list-style-type: none">
	<li><label><input type="checkbox" name="referrer[]" value="online" />
			Online</label></li>
	<li><label><input type="checkbox" name="referrer[]" value="print ad" />
			In a print advertisement</label></li>
	<li><label><input type="checkbox" name="referrer[]" value="web ad" />
			In a web advertisement</label></li>
	<li><label><input type="checkbox" name="referrer[]"
			value="word of mouth" /> Word of mouth</label></li>
	<li><label><input type="checkbox" name="referrer[]"
			value="at conference" /> At another conference</label></li>
	</p>
	<p>
		<input type="submit" name="submit" value="Join the BUCS mailing list" />
	</p>


	</form>