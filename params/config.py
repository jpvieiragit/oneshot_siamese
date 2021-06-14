
class Config:
    """ Exec parameters """
    ## Dataset dirs
    training_dir = "../datasets/openlogo/test_split/train/"
    testing_dir = "../datasets/openlogo/test_split/test/"

    # Alexnet 224,224 following pytorch doc
    im_w = 224
    im_h = 224

    ## Model params
    model = "alexnet"
    #model = "resnet"
    #model = "dense"
    #model = "inception"
    #model = "vgg"
    #model = "squeeze"
    #model = "koch"
    #model = "tests"

    pretrained = False
    distanceLayer = True  # defines if the last layer uses a distance metric or a neuron output
    bceLoss = True  # If true uses Binary cross entropy. Else: contrastive loss

    train_batch_size = 32
    train_number_epochs = 400
    lrate = 0.001

    ## Model save/load paths
    best_model_path = "testmodel.pth"
    model_path = "testmodel_last.pth"

