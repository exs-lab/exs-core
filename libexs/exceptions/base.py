class LibException(Exception):
    def __init__(self, module_name: str, *args: object) -> None:
        self.module_name = module_name
        super().__init__(*args)

    def __str__(self) -> str:
        return f"{self.module_name}: {super().__str__()}"

    def __repr__(self) -> str:
        return f"{self.module_name}: {super().__repr__()}"
