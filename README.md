# Feuille de route Objectif : Récupérer le live de chaine télévisé française et effectuer traitement d'image/parole la dessus.

Description: Création d'une application qui permet de Récupérer des live de chaine télévisé française et puis effectuer des traitement d'image la dessus ( comme : detection de visage , objet , ...) et traitement automatique de la parole ( comme : faire des sous titrage )

la complexité: on ignore la difficulté de Récupérer de live de chaque chaine télévisé Difficulté d'effectuer du traitement d'image sur un live sans engendrer un décalage ou latence Bien comprendre les protocoles de streaming video ( comme dash : Dynamic Adaptive Streaming over HTTP )

Etapes: 1er sprint: Etude sur les différent moyen possible pour Récupérer les live Etude sur les framework de traitement d'image/parole adéquat pour des live ( qui sont assez performant et ne génére pas de latence)

2eme sprint: Implémentation de la fonctionnalité de Récupération de live 3eme sprint: Implémentation du traitement de l'image sur le live 4eme sprint: Implémentation du traitement automatique de la parole

Durée des sprints: une à deux semaines.

POC ( proof of concept ) : https://github.com/bessalahAmar/videoProcessingLiveStreaming

################################################

# Roadmap Objective: To recover the French TV channel live and to perform image / speech processing on it.

Description: Creation of an application that allows you to recover French TV channel live and then perform image processing on top (like: face detection, object, ...) and automatic processing speech (like: do subtitling)

the complexity: we do not know how hard it is to get live from each TV channel Difficulty performing image processing on a live without causing lag or latency Understand video streaming protocols (such as Dynamic Adaptive Streaming over HTTP)

Steps: 1st sprint:     Study on different ways possible to Recover live     Study on the framework of image processing / speech suitable for live (which are quite powerful and does not generate latency)

2nd sprint:     Implementing the Live Recovery feature 3rd sprint:     Implementation of image processing on the live 4th sprint:     Implementation of automatic speech processing

Sprints duration: one to two weeks.

POC (proof of concept): https://github.com/bessalahAmar/videoProcessingLiveStreaming


################################################

# Command :

download images of présentateur France 2 :
python scriptGetImages.py 

extract embedding :
python extract_embeddings.py --dataset dataset --embeddings output/embeddings.pickle --detector face_detection_model --embedding-model openface_nn4.small2.v1.t7

train SVM :
python train_model.py --embeddings output/embeddings.pickle --recognizer output/recognizer.pickle --le output/le.pickle

run global recognizer france 2 :
python f2.py --detector face_detection_model --embedding-model openface_nn4.small2.v1.t7 --recognizer output/recognizer.pickle --le output/le.pickle

################################################

# Credit :

https://www.pyimagesearch.com/2018/09/24/opencv-face-recognition/




