config = {
    "batchsize": 32,
    "num_workers": 1,
    "reload": False,
    "net": "model_resnet",
    "dropout": 0.2,
    "specAugment": [128, 2, 32, 2],
    "lr": 1e-3,
    "eta_min": 1e-5,
    "max_epoch": 200,
    "weight_decay": 1e-5,
    "mixup_alpha": None,
    "out_dir": "./trained_models/",
}
