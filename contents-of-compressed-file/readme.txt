1. Extract the compressed file:
	tar -xvf count-the-days.tar.gz

2. Go to the .count-the-days folder and make sure the .sh and .py files have executable permissions:
	cd .count-the-days
	sudo chmod +x *.[ps][yh]
	to make sure: ls -l

3. Edit the count-the-days.py file to use the date you want to count down to:
	vi count-the-days.py

4. Move the .count-the-days folder to your home directory:
	mv . ~

5. To run, execute the start.sh script:
	sh start.sh.
	Or in the terminal run:
	conky -c ~/.count-the-days/count-the-days.conkyrc

6. To autostart add:
	sh -c "conky -p 15 -c ~/.count-the-days/count-the-days.conkyrc"
	in startup applications. This will pause the start of conky for 15 secs to allow the window manager to load first.

