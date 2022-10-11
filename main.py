def compute_output(inputs, weights, bias):
    output = (
            inputs[0] * weights[0] +
            inputs[1] * weights[1] +
            inputs[2] * weights[2] + bias
    )
    return output


if __name__ == '__main__':
    inputs = [1, 2, 3]
    weights = [0.2, 0.8, -0.5]
    bias = 2
    output = compute_output(inputs, weights, bias)
    print(output)
