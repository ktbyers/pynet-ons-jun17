from __future__ import print_function
import jinja2

my_vars = {
    'juniper1':
            {
                'ge_ip': '10.10.10.1',
                'ge_netmask': '24',
                'local_as': '101',
                'peer_as': '102',
                'peer_ip': '10.10.10.2',
            },
    'juniper2':
            {
                'ge_ip': '10.10.10.2',
                'ge_netmask': '24',
                'local_as': '102',
                'peer_as': '101',
                'peer_ip': '10.10.10.1',
            },
}


template_file = 'build_bgp.j2'
with open(template_file) as f:
    bgp_template = f.read()

for router_id in my_vars:
    template = jinja2.Template(bgp_template)
    rtr_cfg = template.render(my_vars[router_id])
    print()
    print('-' * 60)
    print("This is router: {}".format(router_id))
    print(rtr_cfg)
    print()
