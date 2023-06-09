#include "fann.h"

int main()
{   
    const float learning_rate = 1.e-3;
    const unsigned int num_input = 784;
    const unsigned int num_output = 10;
    const unsigned int num_layers = 3;
    const unsigned int num_neurons_hidden = 300;
    const float desired_error = 0.02;
    const unsigned int max_iterations = 1000;
    const unsigned int epochs_between_reports = 1;

    struct fann *ann = fann_create_standard( num_layers, num_input,  num_neurons_hidden, num_output );

    fann_set_activation_function_hidden( ann, FANN_SIGMOID );
    fann_set_activation_function_output( ann, FANN_SIGMOID );
    fann_set_learning_rate( ann, learning_rate );

    fann_train_on_file(ann, "train.data", max_iterations, epochs_between_reports, desired_error);

    fann_save(ann, "mnist.net");

    fann_destroy(ann);

    return 0;
}