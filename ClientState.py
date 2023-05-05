class ClientState:
    def __init__(self, client):
        # Client config
        self.host = client.host
        self.port = client.port
        self.ip = client.ip

        # Client local dataset
        self.dataset_path = client.dataset_path

        # Client local tensorflow model
        self.model = client.model

    def check(self):
        print(self.host, self.port)
        print(self.dataset_path)

    def check_model(self):
        print("[Snapshot] Current epoch:", self.model.current_epoch)
        print("[Snapshot] Current loss:", self.model.current_loss)
        print("[Snapshot] Current accuracy:", self.model.current_accuracy)
        # print("[Snapshot] Current weights:", self.model.current_weights)

    def show_state_summary(self):
        print("[Summary] Client - {}".format(self.ip))
        print("Dataset:", self.dataset_path)
        print("Current epoch:", self.model.current_epoch)
        print("Current loss:", self.model.current_loss)
        print("Current accuracy:", self.model.current_accuracy)
