"""
*AvaTax Software Development Kit for Python
*
*(c) 2004-2017 Avalara, Inc.
*
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 *
 * @author     Robert Bronson
 * @author     Phil Werner
 * @author     Adrienne Karnoski
 * @author     Han Bao
 * @copyright  2004-2017 Avalara, Inc.
 * @license    https://www.apache.org/licenses/LICENSE-2.0
 * @version    
 * @link       https://github.com/avadev/AvaTax-REST-V2-Python-SDK
 *
 """

from sandbox_client import SandboxClient


class Client(SandboxClient):
    """."""

    def __init__(self, app_name, app_version, machine_name):
        """Init regular client obj."""
        super(Client, self).__init__(app_name, app_version, machine_name)
        self.base_url = 'https://rest.avatax.com'

