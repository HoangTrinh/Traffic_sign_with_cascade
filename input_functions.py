def read_config(config_file):
    config = {}
    plates = {}
    key_names = ['in_video', 'out_video', 'format', 'n_plates', 'from_frame', 'to_frame']

    with open(config_file) as f:
        lines = f.readlines()
        for line in lines:
            all_par = line.split()

            if all_par[0] not in key_names:
                continue

            if all_par[0] == 'n_plates':
                if not int(all_par[1]):
                    return {}
                n_plates = all_par[1]
                for i in range(int(n_plates)):
                    if not float(all_par[i * 3 + 3]) or not int(all_par[i * 3 + 4]):
                        return {}
                    plates[str(all_par[2 + i * 3])] = [float(all_par[i * 3 + 3]), int(all_par[i * 3 + 4])]
            else:
                config[all_par[0]] = all_par[1]

    config['plates'] = plates
    config['from_frame'] = int(config['from_frame'])
    config['to_frame'] = int(config['to_frame'])
    return config
