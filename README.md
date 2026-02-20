# Welcome to DJESTHESIA
Welcome to DJESTHESIA! DJESTHESIA is an innovative interface for DJs that explores the integration of Tangible User Interfaces (TUIs). With DJESTHESIA, we aim to transform the DJ into both a performer and a performance.

## Four Interaction Modes
![](https://cyphy.life/media/prose/2025/05/25/9c95af50-f5c1-4a6f-a4ad-0c124cfaf50a.webp)
1. **Knob changes the music**<br> The DJ changes the music by physically turning knobs.
2. **Music changes visuals**<br> The visuals projected onto the DJ's workspace will change in response to low-latency audio.
3. **Gesture changes visuals**<br> The Motion Capture (MoCap) system tracks gestures of hands with MoCap marker gloves that interact with the generated visuals.
4. **Gesture changes music**<br> With two-handed gestures, a DJ can draw EQ curves to be applied to the music.<br>


## Workflow (Visuals)
![](https://cyphy.life/media/prose/2025/05/25/b01af4f0-9a81-49d7-8104-2560a25db1b4.webp?content-disposition=attachment)
1. **Sensing**: The system uses a motion capture camera system (OptiTrack) to track the position and orientation of the Universal Marker Holders (UMHs). UMHs are normally place inside a glove to track the hands and gestures of the DJ. However, they could also be located on top of the mixer or the decks to capture the interactions between the DJ and the equipment. This information is sent to a tracking software (Motive 3D) for processing. 
2. **Processing**: A server running the Robot Operating System (ROS) serves as an intermediary between the physical and digital information by processing the motion capture data and sending it to the visualization engine software via UDP. 
3. **Actuation**: The visualization engine is a WEBGL fluid simulation software programmed in Javascript (JS). This software receives the position and orientation coordinates of the UMHs and maps them into the computer mouse positions. Then, the mouse receives a triggering signal from the audio analyzer. If it passes the threshold, the mouse will trigger a click. If not, the mouse will just follow the UMH coordinates. Finally, this information is projected onto the table where the DJ is performing.


## Gallery
<table><tr><td><img src="https://cyphy.life/media/filer_public/f9/bb/f9bb42ec-3f26-4eef-a478-bfd1e1f2f823/1.png"></td><td><img src="https://cyphy.life/media/filer_public/5f/98/5f98059e-e201-402d-bbe1-b577f5184ae7/2.png"></td></tr><tr><td><image src=https://cyphy.life/media/filer_public/3b/be/3bbe6044-a172-4805-a9e6-481985a35a74/3.png></td><td><image src=https://cyphy.life/media/filer_public/c6/18/c6181485-4e7c-4cfc-8988-e5f80f23c329/4.png></td></tr><tr><td><image src=https://cyphy.life/media/filer_public/39/11/39119670-4963-4684-8974-8f99d2febe93/5.png></td><td><image src=https://cyphy.life/media/filer_public/09/3b/093b85a9-fbca-4bc1-9d8e-485b2ff05866/6.png></td></tr></table>


## Video

Watch the YouTube video about DJESTHESIA!

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/Y5tWjAqEkEU/0.jpg)](https://www.youtube.com/watch?v=Y5tWjAqEkEU)

## Components
| Component | Description | Code |
| ------------- | ------------- | ------------- |
| OptiTrack | Tracking system for the tangible objects | [OptiTrack](https://github.com/IERoboticsAILab/optitrack_ros_communication)| 

## Paper
The paper for this project can be found here.
- [Website](https://dl.acm.org/doi/10.1145/3721243.3735980)
- [pdf](https://hdl.handle.net/20.500.14417/3841)


## Contact
For any questions or inquiries, please contact us at eduardo.castello@ie.edu or sono.ieu2023@student.ie.edu.
