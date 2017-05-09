import numpy as np

subset = np.array([[[  1.,   2.,   3.,   4.,   5.],
                    [ 21.,  21.,  21.,  21.,  21.]],
                   [[ 12.,  12.,  12.,  12.,  12.],
                    [ 22.,  22.,  22.,  22.,  22.]],
                   [[ 13.,  13.,  13.,  13.,  13.],
                    [ 23.,  23.,  23.,  23.,  23.]]])

single_band = np.array([[  1.,  21.,  31.],
                        [ 12.,  22.,  32.],
                        [ 13.,  23.,  33.],
                        [ 14.,  24.,  34.],
                        [ 15.,  25.,  35.]])

data_value = np.array([[[  1.,   2.],
                        [ 21.,  21.],
                        [ 31.,  31.]],
                       [[ 12.,  12.],
                        [ 22.,  22.],
                        [ 32.,  32.]],
                       [[ 13.,  13.],
                        [ 23.,  23.],
                        [ 33.,  33.]],
                       [[ 14.,  14.],
                        [ 24.,  24.],
                        [ 34.,  34.]],
                       [[ 15.,  15.],
                        [ 25.,  25.],
                        [ 35.,  35.]]])

nonmasked_array = \
            np.array([[[  1.00000000e+00,   2.00000000e+00,   3.00000000e+00,  4.00000000e+00],
                       [  2.10000000e+01,   2.10000000e+01,   2.10000000e+01, 2.10000000e+01],
                       [  3.10000000e+01,   3.10000000e+01,   3.10000000e+01, 3.10000000e+01],
                       [  4.10000000e+01,   4.10000000e+01,   4.10000000e+01, 4.10000000e+01],
                       [  5.10000000e+01,   5.10000000e+01,   5.10000000e+01, 5.10000000e+01]],
                      [[  1.20000000e+01,   1.20000000e+01,   1.20000000e+01, 1.20000000e+01],
                       [  2.20000000e+01,   2.20000000e+01,   2.20000000e+01, 2.20000000e+01],
                       [  3.20000000e+01,   3.20000000e+01,   3.20000000e+01, 3.20000000e+01],
                       [  4.20000000e+01,   4.20000000e+01,   4.20000000e+01, 4.20000000e+01],
                       [  5.20000000e+01,   5.20000000e+01,   5.20000000e+01, 5.20000000e+01]],
                      [[  1.30000000e+01,   1.30000000e+01,   1.30000000e+01, 1.30000000e+01],
                       [  2.30000000e+01,   2.30000000e+01,   2.30000000e+01, 2.30000000e+01],
                       [  3.30000000e+01,   3.30000000e+01,   3.30000000e+01, 3.30000000e+01],
                       [  4.30000000e+01,   4.30000000e+01,   4.30000000e+01, 4.30000000e+01],
                       [ -9.99900000e+03,  -9.99900000e+03,  -9.99900000e+03, -9.99900000e+03]],
                      [[  1.40000000e+01,   1.40000000e+01,   1.40000000e+01, 1.40000000e+01],
                       [  2.40000000e+01,   2.40000000e+01,   2.40000000e+01, 2.40000000e+01],
                       [  3.40000000e+01,   3.40000000e+01,   3.40000000e+01, 3.40000000e+01],
                       [ -9.99900000e+03,  -9.99900000e+03,  -9.99900000e+03, -9.99900000e+03],
                       [ -9.99900000e+03,  -9.99900000e+03,  -9.99900000e+03, -9.99900000e+03]],
                      [[  1.50000000e+01,   1.50000000e+01,   1.50000000e+01, 1.50000000e+01],
                       [  2.50000000e+01,   2.50000000e+01,   2.50000000e+01, 2.50000000e+01],
                       [ -9.99900000e+03,  -9.99900000e+03,  -9.99900000e+03, -9.99900000e+03],
                       [ -9.99900000e+03,  -9.99900000e+03,  -9.99900000e+03, -9.99900000e+03],
                       [ -9.99900000e+03,  -9.99900000e+03,  -9.99900000e+03, -9.99900000e+03]]])

masked_array = \
         np.array([[[False, False, False, False],
                    [False, False, False, False],
                    [False, False, False, False],
                    [False, False, False, False],
                    [False, False, False, False]],
                   [[False, False, False, False],
                    [False, False, False, False],
                    [False, False, False, False],
                    [False, False, False, False],
                    [False, False, False, False]],
                   [[False, False, False, False],
                    [False, False, False, False],
                    [False, False, False, False],
                    [False, False, False, False],
                    [ True,  True,  True,  True]],
                   [[False, False, False, False],
                    [False, False, False, False],
                    [False, False, False, False],
                    [ True,  True,  True,  True],
                    [ True,  True,  True,  True]],
                   [[False, False, False, False],
                    [False, False, False, False],
                    [ True,  True,  True,  True],
                    [ True,  True,  True,  True],
                    [ True,  True,  True,  True]]])

rdc_get_data = \
        [[[[ 100.,  2.], [  21., 21.], [  31., 31.]],
          [[  12., 12.], [  22., 22.], [  32., 32.]],
          [[  13., 13.], [  23., 23.], [  33., 33.]],
          [[  14., 14.], [  24., 24.], [  34., 34.]],
          [[  15., 15.], [  25., 25.], [  35., 35.]]],
         [[[ 200.,  2.], [  21., 21.], [  31., 31.]],
          [[  12., 12.], [  22., 22.], [  32., 32.]],
          [[  13., 13.], [  23., 23.], [  33., 33.]],
          [[  14., 14.], [  24., 24.], [  34., 34.]],
          [[  15., 15.], [  25., 25.], [  35., 35.]]],
         [[[ 300.,  2.], [  21., 21.], [  31., 31.]],
          [[  12., 12.], [  22., 22.], [  32., 32.]],
          [[  13., 13.], [  23., 23.], [  33., 33.]],
          [[  14., 14.], [  24., 24.], [  34., 34.]],
          [[  15., 15.], [  25., 25.], [  35., 35.]]]]

rdc_get_data_single_band = \
        [[[ 100.,  100.,  100.],
          [  12.,   22.,   32.],
          [  13.,   23.,   33.],
          [  14.,   24.,   34.],
          [  15.,   25.,   35.]],
         [[ 200.,  200.,  200.],
          [  12.,   22.,   32.],
          [  13.,   23.,   33.],
          [  14.,   24.,   34.],
          [  15.,   25.,   35.]],
         [[ 300.,  300.,  300.],
          [  12.,   22.,   32.],
          [  13.,   23.,   33.],
          [  14.,   24.,   34.],
          [  15.,   25.,   35.]]]

rdc_get_data_window = \
        [[[[ 100.,  2.], [  21., 21.], [  31., 31.]],
          [[  12., 12.], [  22., 22.], [  32., 32.]]],
         [[[ 200.,  2.], [  21., 21.], [  31., 31.]],
          [[  12., 12.], [  22., 22.], [  32., 32.]]],
         [[[ 300.,  2.], [  21., 21.], [  31., 31.]],
          [[  12., 12.], [  22., 22.], [  32., 32.]]]]

rdc_get_data_window_single_band = \
        [[[ 100., 100., 100.],
          [  12.,  22.,  32.]],
         [[ 200., 200., 200.],
          [  12.,  22.,  32.]],
         [[ 300., 300., 300.],
          [  12.,  22.,  32.]]]
