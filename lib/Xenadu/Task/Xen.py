import Xenadu
from Xenadu.Task.Ssh import ssh_dom0

def xen_create_image(dummy):
    #xen_tools_cmd = "/usr/bin/xen-create-image --hostname=%(hostname)s --ip=%(ip)s --output=/etc/xen/domains --no-hosts " + \
    #    "--swap=%(swap)sMb --memory=%(ram)sMb --size=%(disk)sMb --verbose --force --boot"
    xen_tools_cmd = "/usr/bin/xen-create-image --hostname=%(hostname)s --ip=%(ip)s --output=/etc/xen/domains --no-hosts " + \
        "--swap=%(swap)sMb --memory=%(ram)sMb --size=%(disk)sMb --verbose --force"
    ssh_dom0(xen_tools_cmd % Xenadu.Env["Core"].config["xen"])
    
    set_auto_cmd = "ln -s /etc/xen/domains/%(hostname)s.cfg /etc/xen/auto" % Xenadu.Env["Core"].config["xen"]
    ssh_dom0(set_auto_cmd)

def register():
	Xenadu.Env["Core"].registry.register_task(name="guest.create", args=0, help="create xen guest", function=xen_create_image)
