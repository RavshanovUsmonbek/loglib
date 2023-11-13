import importlib


def enable_loggings(context):
    for key in context.settings.get("logging", {}).keys():
        try:
            module = importlib.import_module(f"{key}.enabler")
            fn = getattr(module, f"enable_{key}_logging")
            fn(context)
        except Exception as e:
            print(e)
            print(f"FAILED to load module {key}")
