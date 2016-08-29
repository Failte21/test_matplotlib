def convert_range(value, in_min, in_max, out_min, out_max):
    return float((float(value - in_min) / float(in_max - in_min))
         * (out_max - out_min) + out_min);
