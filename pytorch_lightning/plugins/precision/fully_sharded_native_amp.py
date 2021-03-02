# Copyright The PyTorch Lightning team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from typing import Any, Union

from torch.optim import Optimizer

from pytorch_lightning.plugins.precision.sharded_native_amp import ShardedNativeMixedPrecisionPlugin


class FullyShardedNativeMixedPrecisionPlugin(ShardedNativeMixedPrecisionPlugin):
    """Mixed Precision for Full Sharded Training"""

    def clip_gradients(
        self, model: Any, optimizer: Optimizer, clip_val: Union[int, float], norm_type: float = float(2.0)
    ) -> None:
        # Model manages clipping of gradients
        model.clip_grad_norm_(clip_val, norm_type)
