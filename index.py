head = {
    "value": 11,
    "next": {
        "value": 12,
        "next": {
            "value": 13,
            "next": {
                "value": 14,
                "next": {"value": 15, "next": {"value": 16, "next": None}},
            },
        },
    },
}

print(head["next"]["next"]["next"]["value"])
