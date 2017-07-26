# BCI Media player
BCI-Operated Media Player is a mp3 player that can be controlled through a
brain-computer interface (BCI). It has been designed for patients who are severely
impaired and partially or completely locked in. They have lost all motor ability but have
active brains. In our media player, we have created four controls that have been encoded
as a combination of left-hand and right-hand movements. The OpenBCI device reads the
input in the form of EEG signals from the patient’s brain and then uses the same to
control the media player. It is easily scalable to multiple controls through a binary-like
combination.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisities
* Basic knowledge of python scripting 

### Installing:

1. Install python 2.7
..* Note: While installing, check the option to add Python to the path variable
2. Install numpy
 ```
pip install numpy
```
3. Install scipy package
4. Install scikit-learn package
5. Install wyrm package
```
pip install wyrm
```
6.Install mp3play package


```
pip install mp3play
```
While running:
Before running the files, add the music you would like to play to the “songs” folder. All the music must be in mp3 format only. 
```
1. run the gui_final.py file using the following command in the command prompt-
	python gui_final.py <string_of_0s_and 1s>
For example,
python gui_final.py 01
2. run the bci_final.py file using the following command in the command prompt-
	python bci_final.py 
```
### Screenshots 
![Media Player Screen 1](http://i.imgur.com/M7GT8NH.jpg "Media Player Screen 1")

### Contributing
* File an issue
* Assign it to yourself or anyone who's interested 
* Fork the repository
* Make changes and send a pull request
* If everything is good, the PR will get merged



### Authors
* **Bhoomika Agarwal** - *Initial work* - [Bhoom10](https://github.com/bhoom10)


## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/bhoom10/bci-media-player/blob/master/LICENSE) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc



