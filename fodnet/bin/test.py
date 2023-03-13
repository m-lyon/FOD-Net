"""FOD-Net
Fiber orientation distribution super resolution
Licensed under the CC BY-NC-SA 4.0 License (see LICENSE for details)
Written by Rui Zeng @ The University of Sydney (r.zeng@outlook.com / rui.zeng@sydney.edu.au)


"""
import nibabel as nib

from fodnet.data.hcp_dataset import flip_axis_to_match_HCP_space
from fodnet.models.fodnet_model import fodnetModel
from fodnet.options.test_options import TestOptions


def run_test_inference(opt):
    '''Run test inference for FOD-Net'''
    fodlr_file = nib.load(opt.fod_path)
    brain_mask_file = nib.load(opt.brain_mask_path)

    fixed_fodlr, fixed_fodlr_affine, _ = flip_axis_to_match_HCP_space(
        fodlr_file.get_fdata(), fodlr_file.affine
    )

    fixed_brain_mask, _, _ = flip_axis_to_match_HCP_space(
        brain_mask_file.get_fdata(), brain_mask_file.affine
    )

    if fixed_fodlr.shape[:3] != fixed_brain_mask.shape:
        raise AttributeError('Input fod and mask should have the same shape')

    model = fodnetModel(opt)
    model.load_weights(weights_path=opt.weights_path)
    model.eval()
    model.set_input_for_test(fixed_fodlr, fixed_brain_mask, fixed_fodlr_affine, fodlr_file.header)
    model.test(opt.output_path)


if __name__ == '__main__':
    opts = TestOptions().parse()
    run_test_inference(opts)
