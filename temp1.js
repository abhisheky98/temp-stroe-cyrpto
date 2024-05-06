// Check if MetaMask is installed
if (!window.ethereum) {
    console.error('MetaMask is not installed');
  } else {
    const provider = new ethers.providers.Web3Provider(window.ethereum);
  
    const ethereumButton = document.querySelector('.enableEthereumButton');
    const sendEthButton = document.querySelector('.sendEthButton');
    let accounts = [];
  
    // Send Ethereum to an address.
    sendEthButton.addEventListener('click', () => {
      provider
        .send('eth_sendTransaction', [
          {
            // The user's active address.
            from: '0xE22a6Fab98170621B01C0bC44B2C97F07f428d31',
            // Required except during contract publications.
            to: '0x8200c5553387cD790385A283a8aDB2916566c853',
            // Only required to send ether to the recipient from the initiating external account.
            value: ethers.utils.parseEther('0.0004').toHexString(),
            // Customizable by the user during MetaMask confirmation.
            gasLimit: '500000',
            // Customizable by the user during MetaMask confirmation.
            maxPriorityFeePerGas: '2000',
            // Customizable by the user during MetaMask confirmation.
            maxFeePerGas: '10000',
          },
        ])
        .then((txHash) => console.log(txHash))
        .catch((error) => console.error(error));
    });
  
    ethereumButton.addEventListener('click', () => {
      getAccount();
    });
  
    async function getAccount() {
      accounts = await provider.send('eth_requestAccounts', []);
    }
  }