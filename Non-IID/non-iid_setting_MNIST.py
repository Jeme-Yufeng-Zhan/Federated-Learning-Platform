import torchvision.datasets as dsets 
import torchvision.transforms as transforms

def load_dataset():
	# pass
	trainset = dsets.MNIST(root = '/data/MNIST', train = True, transform = transforms.ToTensor(), download = True)
	testset = dsets.MNIST(root = '/data/MNIST', train = False, transform = transforms.ToTensor(), download = True)
	return trainset, testset
#non-iid setting@ each client has one class or two class
def non-iid_setting(trainset, per_class):
	# pass
	


if __name__ == "__main__":
	# pass
	load_dataset()
