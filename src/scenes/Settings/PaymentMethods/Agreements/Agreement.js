import React from 'react'
import KevinAgreement from './Kevin/KevinAgreement.js'
import MobilepayAgreement from './Mobilepay/MobilepayAgreement.js'
import MobilepaySubscriptionAgreement from './MobilepaySubscription/MobilepaySubscriptionAgreement.js'
import Integration from './Integration/Integration.js'
import External from './External/External.js'


const Agreement = ({method}) => {
  return <>
            {
              method === "external" && <External/>
            }
            {
              method === "mobilepay" && <MobilepayAgreement/>
            }
            {
              method === "mobilepaysubscription" && <MobilepaySubscriptionAgreement/>
            }
            {
              method === "integration" && <Integration/>
            }
            {
              method === "kevin" && <KevinAgreement/>
            }
  </>
}

export default Agreement