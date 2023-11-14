def ft_tqdm(lst):
    """A basic tqdm-like function that works with any iterable."""
    length = len(lst)
    for i in lst:
        yield i

        percent = (i + 1) / len(lst)
        progress = int(percent * 50)

        print(
            "{:3d}%|{}| {}/{}]".format(
                int(percent * 100),
                progress * "█" + (50 - progress) * " ",
                i + 1,
                length,
            ),
            end="\r",
        )
