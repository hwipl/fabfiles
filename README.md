# Fabfiles

Some fabfiles for executing shell commands on (remote) hosts. See
[Fabric](https://www.fabfile.org) for more information about Fabric and its
installation and configuration.

## Usage

* List tasks: `fab --list`
* Run task on local host: `fab <task>`
* Run task on remote host(s): `fab -H <host(s)> <task>`

`<task>` is the name of the task as shown by `fab --list`.
`<host(s)>` is a comma separated list of host names or IP addresses.

### Examples

Run command on local host:
`fab archlinux.get-installed-packages`

Run command via SSH on specific host:
`fab -H localhost archlinux.get-installed-packages`
