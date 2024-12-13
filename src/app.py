from collections import defaultdict
from flask import Flask, request, jsonify
from storage import log_request

app = Flask(__name__)


def find_unique_pairs_with_equal_sum(arr):
    sum_dict = defaultdict(set)

    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            pair_sum = arr[i] + arr[j]
            pair = tuple(sorted((arr[i], arr[j])))
            sum_dict[pair_sum].add(pair)

    results = []
    for pair_sum, pairs in sum_dict.items():
        if len(pairs) > 1:  # Only consider sums with more than one unique pair
            results.append(
                {"sum": pair_sum, "pairs": [list(pair) for pair in pairs]}
            )

    return results


@app.route("/assignment", methods=["POST"])
def assignment():
    data = request.get_json()

    log_request(data)

    if not data or "data" not in data:
        return (
            jsonify(
                {
                    "error": 'Invalid input. Please provide a "data" field with a list of numbers.'  # noqa
                }
            ),
            400,
        )

    arr = data["data"]  # test comment

    # Validate that the input is a list of numbers
    if not isinstance(arr, list) or not all(
        isinstance(x, (int, float)) for x in arr
    ):
        return (
            jsonify({"error": 'The "data" field must be a list of numbers.'}),
            400,
        )

    results = find_unique_pairs_with_equal_sum(arr)

    return jsonify({"results": results})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
