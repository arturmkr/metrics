import psutil
import argparse

def print_cpu_metrics():
    cpu_times = psutil.cpu_times()
    print("system.cpu.idle", cpu_times.idle)
    print("system.cpu.user", cpu_times.user)
    print("system.cpu.guest", cpu_times.guest)
    print("system.cpu.iowait", cpu_times.iowait)
    print("system.cpu.stolen", cpu_times.steal)
    print("system.cpu.system", cpu_times.system)

def print_mem_metrics():
    virtual_mem = psutil.virtual_memory()
    swap_mem = psutil.swap_memory()
    print("virtual total", virtual_mem.total)
    print("virtual used", virtual_mem.used)
    print("virtual free", virtual_mem.free)
    print("virtual shared", virtual_mem.shared)
    print("swap total", swap_mem.total)
    print("swap used", swap_mem.used)
    print("swap free", swap_mem.free)

def metrics_main(metric_type):
    if metric_type == 'cpu':
        print_cpu_metrics()
    elif metric_type == 'mem':
        print_mem_metrics()

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Print system metrics.')
    parser.add_argument('metric', choices=['cpu', 'mem'], help='Type of metric to print')
    args = parser.parse_args()
    metrics_main(args.metric)
